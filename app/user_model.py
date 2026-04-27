from dataclasses import dataclass
from typing import Optional
<<<<<<< HEAD
from .db import get_connection

ALLOWED_ROLES = {"Admin", "Manager", "User"}

=======

from .db import get_connection


ALLOWED_ROLES = {"Admin", "Manager", "User"}


>>>>>>> upstream/main
@dataclass
class UserCreate:
    name: str
    identifier: str
    password_hash: str
    role: str
    two_fa_secret: str

<<<<<<< HEAD
def split_identifier(identifier: str) -> tuple[Optional[str], Optional[str]]:
    value = identifier.strip()
    if "@" in value: return value.lower(), None
    return None, value.lower()

=======

def split_identifier(identifier: str) -> tuple[Optional[str], Optional[str]]:
    value = identifier.strip()
    if "@" in value:
        return value.lower(), None
    return None, value.lower()


>>>>>>> upstream/main
def create_user(payload: UserCreate) -> int:
    email, username = split_identifier(payload.identifier)
    conn = get_connection()
    try:
        cur = conn.execute(
<<<<<<< HEAD
            "INSERT INTO users (name, email, username, password_hash, role, two_fa_secret) VALUES (?, ?, ?, ?, ?, ?)",
            (payload.name.strip(), email, username, payload.password_hash, payload.role, payload.two_fa_secret)
=======
            """
            INSERT INTO users (name, email, username, password_hash, role, two_fa_secret)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                payload.name.strip(),
                email,
                username,
                payload.password_hash,
                payload.role,
                payload.two_fa_secret,
            ),
>>>>>>> upstream/main
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()

<<<<<<< HEAD
=======

>>>>>>> upstream/main
def find_by_identifier(identifier: str):
    email, username = split_identifier(identifier)
    conn = get_connection()
    try:
<<<<<<< HEAD
        if email: row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        else: row = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
=======
        if email:
            row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        else:
            row = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
>>>>>>> upstream/main
        return dict(row) if row else None
    finally:
        conn.close()

<<<<<<< HEAD
=======

>>>>>>> upstream/main
def find_by_id(user_id: int):
    conn = get_connection()
    try:
        row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()
<<<<<<< HEAD

def update_last_2fa(user_id: int, time_step: int):
    conn = get_connection()
    try:
        conn.execute("UPDATE users SET last_2fa_at = ? WHERE id = ?", (time_step, user_id))
        conn.commit()
    finally:
        conn.close()
=======
>>>>>>> upstream/main
