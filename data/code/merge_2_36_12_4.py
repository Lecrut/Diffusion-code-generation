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
    host: str = "localhost"
    port: int = 6379
    max_size_mb: int = 500
    ttl_seconds: int = 3600
@dataclass(frozen=True)
class LoggingConfig:
    level: str = "INFO"
    format_str: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: str = "/var/log/app.log"
def get_configuration() -> tuple[DatabaseConfig, CacheConfig, LoggingConfig]:
    return DatabaseConfig(), CacheConfig(), LoggingConfig()
if __name__ == '__main__':
    db_cfg, cache_cfg, log_cfg = get_configuration()
    print(f"DB: {db_cfg.host}:{db_cfg.port}, User={db_cfg.user}")
    print(f"Cache: {cache_cfg.host}:{cache_cfg.port}, Size={cache_cfg.max_size_mb}MB")
    print(f"Log Level: {log_cfg.level}, File: {log_cfg.file_path}")