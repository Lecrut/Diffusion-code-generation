def compiler(code) -> bool:
    try:
        compile(code, "<string>", "exec")
        return True
    except Exception:
        return False