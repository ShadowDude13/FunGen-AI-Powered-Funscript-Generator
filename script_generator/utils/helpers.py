import platform


def is_mac():
    return platform.system() == "Darwin"

def to_int_or_none(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None