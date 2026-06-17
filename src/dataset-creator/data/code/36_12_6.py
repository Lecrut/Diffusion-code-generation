import dataclasses
@dataclasses.dataclass(frozen=True)
class AppConfig:
    app_name: str = "ProductionApp"
    environment: str = "production"
    debug_mode: bool = False
    max_connections: int = 100
    timeout_seconds: float = 30.0
@dataclasses.dataclass(frozen=True)
class DatabaseConfig(AppConfig):
    host: str = "localhost"
    port: int = 5432
    database_name: str = "main_db"
    username: str = "admin"
    password_hash: str = "$2b$10$r7FkbVHqP9jLmNkXwZvQy.8YzGhJfKlMnOpQrStUvWxYzAbCdEfGhi"
@dataclasses.dataclass(frozen=True)
class CacheConfig(AppConfig):
    backend: str = "redis"
    server_address: str = "127.0.0.1"
    cache_ttl_seconds: int = 3600
if __name__ == '__main__':
    config = DatabaseConfig()
    print(f"{config.app_name} running in {config.environment}")
    print(f"DB Host: {config.host}:{config.port}, DB Name: {config.database_name}")