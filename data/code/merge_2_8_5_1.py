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
    def __init__(self, handlers: List[Callable[[Any], None]]):
        self._lock = threading.Lock()
        self.handlers = handlers
    def _log(self, level: Severity, message: str) -> None:
        with self._lock:
            for handler in self.handlers:
                if callable(handler):
                    try:
                        handler(level, message)
                    except Exception as e:
                        print(f"Handler error: {e}")
    def debug(self, msg: Any) -> None:
        self._log(Severity.DEBUG, str(msg))
    def info(self, msg: Any) -> None:
        self._log(Severity.INFO, str(msg))
    def warning(self, msg: Any) -> None:
        self._log(Severity.WARNING, str(msg))
    def error(self, msg: Any) -> None:
        self._log(Severity.ERROR, str(msg))
    def critical(self, msg: Any) -> None:
        self._log(Severity.CRITICAL, str(msg))
class ConsoleHandler:
    def __init__(self):
        pass
    def handle(self, level: Severity, message: str) -> None:
        prefix = {
            Severity.DEBUG: "[DEBUG]",
            Severity.INFO: "[INFO]",
            Severity.WARNING: "[WARNING]",
            Severity.ERROR: "[ERROR]",
            Severity.CRITICAL: "[CRITICAL]"
        }.get(level, "UNKNOWN")
        print(f"{prefix} - {message}")
class FileHandler:
    def __init__(self):
        self.file = open("app.log", "a", encoding="utf-8")
    def handle(self, level: Severity, message: str) -> None:
        timestamp = "[TIMESTAMP]"                                               
        print(f"{timestamp} {level.name}: {message}", file=self.file)
def main():
    logger = ThreadSafeLogger([ConsoleHandler(), FileHandler()])
    logger.debug("Debug message sample")
    logger.info("Info message sample")
    logger.warning("Warning threshold reached")
    logger.error("An error occurred during execution")
    logger.critical("System failure imminent")
if __name__ == '__main__':
    main()