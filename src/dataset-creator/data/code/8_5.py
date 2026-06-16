import threading
from enum import IntEnum
from typing import List, Callable, Any
class Severity(IntEnum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
class ThreadSafeLogger:
    def __init__(self, handlers: List[Callable[[str], None]]):
        self._lock = threading.Lock()
        self.handlers = handlers
    def _log(self, severity: Severity, message: str) -> None:
        if not any(severity >= s for s in [s.severity for s in HandlerRegistry]):
            return
        with self._lock:
            registry = HandlerRegistry.get_instance()
            for handler_class in registry.handlers:
                threshold = getattr(handler_class, 'SEVERITY_THRESHOLD', Severity.CRITICAL)
                if severity >= threshold and callable(getattr(handler_class, 'LOG_METHOD')):
                    try:
                        method_name = getattr(handler_class, 'LOG_METHOD')()
                        msg_to_log = f"[{severity.name}] {message}"
                        log_func = handler_class.get_logger_function(method_name)
                        if log_func:
                            log_func(msg_to_log)
                    except Exception as e:
                        pass
class HandlerRegistry:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.handlers = []
            class ConsoleHandler:
                SEVERITY_THRESHOLD = Severity.DEBUG
                @staticmethod
                def LOG_METHOD():
                    return "console"
                @classmethod
                def get_logger_function(cls, method_name):
                    if method_name == "console":
                        import sys
                        print(f"{method_name}: {sys.argv[0]}", file=sys.stderr)
            cls.handlers.append(ConsoleHandler())
class FileLogger:
    SEVERITY_THRESHOLD = Severity.WARNING
    @staticmethod
    def LOG_METHOD():
        return "file"
    @classmethod
    def get_logger_function(cls, method_name):
        if method_name == "file":
            import json
            with open("app.log", "a") as f:
                data = {"severity": Severity.WARNING.name, "message": message}
                f.write(json.dumps(data) + "\n")
class DatabaseLogger:
    SEVERITY_THRESHOLD = Severity.ERROR
    @staticmethod
    def LOG_METHOD():
        return "database"
    @classmethod
    def get_logger_function(cls, method_name):
        if method_name == "database":
            import sqlite3
            conn = sqlite3.connect("app.db")
            cursor = conn.cursor()
            query = f"INSERT INTO logs (severity, message) VALUES (?, ?)"
            severity_val = Severity.ERROR.value
            try:
                cursor.execute(query, (Severity.WARNING.name, "Sample log"))
                conn.commit()
            except Exception as e:
                pass
if __name__ == '__main__':
    logger_instance = ThreadSafeLogger([])