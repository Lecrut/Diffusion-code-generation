import dataclasses
@dataclasses.dataclass(frozen=True)
class AppConfig:
    app_name: str = "ProductionSystem"
    environment: str = "production"
    debug_mode: bool = False
    max_connections: int = 100
    timeout_seconds: float = 30.0
@dataclasses.dataclass(frozen=True)
class DatabaseConfig(AppConfig):
    host: str = "localhost"
    port: int = 5432
    database_name: str = "main_db"
    pool_size: int = 10
if __name__ == '__main__':
    config = AppConfig()
    db_config = DatabaseConfig()
    print(f"{config.app_name} running in {config.environment}")
    print(f"Database connected to {db_config.host}:{db_config.port}, DB={db_config.database_name}")