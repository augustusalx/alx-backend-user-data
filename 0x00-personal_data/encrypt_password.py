#!/usr/bin/env python3
"""To encrypt passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """See if it was formed from the given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
