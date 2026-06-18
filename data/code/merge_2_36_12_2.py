from dataclasses import dataclass
@dataclass(frozen=True)
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    name: str = "production_db"
@dataclass(frozen=True)
class CacheConfig:
    enabled: bool = True
    ttl_seconds: int = 3600
    backend: str = "redis"
@dataclass(frozen=True)
class LoggingConfig:
    level: str = "INFO"
    format_str: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: str = "/var/log/app.log"
def get_configuration() -> tuple[DatabaseConfig, CacheConfig, LoggingConfig]:
    return DatabaseConfig(), CacheConfig(), LoggingConfig()
if __name__ == '__main__':
    db_cfg, cache_cfg, log_cfg = get_configuration()
    print(f"DB: {db_cfg.host}:{db_cfg.port}, Name: {db_cfg.name}")
    print(f"Cache: Enabled={cache_cfg.enabled}, TTL={cache_cfg.ttl_seconds}s")
    print(f"Log Level: {log_cfg.level} -> File: {log_cfg.file_path}")