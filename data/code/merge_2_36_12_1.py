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
    host: str = "redis-server.internal"
    port: int = 6379
    db_index: int = 0
    max_connections: int = 100
@dataclass(frozen=True)
class LoggingConfig:
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: str = "/var/log/app/application.log"
def get_configuration() -> tuple[DatabaseConfig, CacheConfig, LoggingConfig]:
    return DatabaseConfig(), CacheConfig(), LoggingConfig()
if __name__ == '__main__':
    db_cfg, cache_cfg, log_cfg = get_configuration()
    print(f"Database: {db_cfg.host}:{db_cfg.port}, DB={db_cfg.name}")
    print(f"Cache: {cache_cfg.host}:{cache_cfg.port}, DB={cache_cfg.db_index}")
    print(f"Logging Level: {log_cfg.level} -> File: {log_cfg.file_path}")
    assert db_cfg == DatabaseConfig()
    assert cache_cfg == CacheConfig()
    assert log_cfg == LoggingConfig()