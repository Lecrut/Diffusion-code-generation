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
    def _log(self, level: Severity, message: str) -> bool:
        if not any(level >= h.min_level for h in self.handlers):
            return False
        with self._lock:
            for handler in self.handlers:
                try:
                    handler(message)
                except Exception as e:
                    print(f"Handler error: {e}")
        return True
    def debug(self, message: str) -> bool:
        return self._log(Severity.DEBUG, f"[DEBUG] {message}")
    def info(self, message: str) -> bool:
        return self._log(Severity.INFO, f"[INFO] {message}")
    def warning(self, message: str) -> bool:
        return self._log(Severity.WARNING, f"[WARNING] {message}")
    def error(self, message: str) -> bool:
        return self._log(Severity.ERROR, f"[ERROR] {message}")
    def critical(self, message: str) -> bool:
        return self._log(Severity.CRITICAL, f"[CRITICAL] {message}")
class ConsoleHandler:
    min_level = Severity.DEBUG
    def __init__(self):
        pass
    def handle(self, message: str) -> None:
        print(message)
class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename
    def handle(self, message: str) -> None:
        with open(self.filename, 'a') as f:
            f.write(f"{message}\n")
def main():
    console_handler = ConsoleHandler()
    file_handlers = [FileHandler("app.log"), FileHandler("errors.log")]
    logger = ThreadSafeLogger([console_handler] + list(file_handlers))
    if not logger.debug("System initialized"):
        print("Debug logging failed")
    if not logger.info("User logged in successfully"):
        print("Info logging failed")
    if not logger.warning("Disk space running low on server-01"):
        print("Warning logging failed")
    if not logger.error("Database connection timeout after 30s"):
        print("Error logging failed")
    if not logger.critical("Service shutdown initiated due to memory overflow"):
        print("Critical logging failed")
if __name__ == '__main__':
    main()