from dataclasses import dataclass
@dataclass(frozen=True)
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    name: str = "production_db"
    user: str = "admin_user"
    password: str = "secure_password_123!"
@dataclass(frozen=True)
class CacheConfig:
    server_address: tuple[str, int] = ("redis-server", 6379)
    max_size: int = 10000
    ttl_seconds: int = 3600
@dataclass(frozen=True)
class LoggingConfig:
    level: str = "INFO"
    format_str: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: str | None = "/var/log/app.log"
def get_configuration() -> tuple[DatabaseConfig, CacheConfig, LoggingConfig]:
    return DatabaseConfig(), CacheConfig(), LoggingConfig()
if __name__ == '__main__':
    db_cfg, cache_cfg, log_cfg = get_configuration()
    print(f"Database: {db_cfg.host}:{db_cfg.port}, DB={db_cfg.name}")
    print(f"Cache: {cache_cfg.server_address[0]}:{cache_cfg.server_address[1]}, Size={cache_cfg.max_size}")
    print(f"Log Level: {log_cfg.level} at {log_cfg.file_path}")
    assert db_cfg.host == "localhost", "Host mismatch"
    assert cache_cfg.ttl_seconds == 3600, "TTL mismatch"