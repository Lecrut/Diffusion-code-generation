import os
class ConfigManager:
    def __init__(self):
        self.config = {
            'mode': 'debug',
            'log_level': 'INFO'
        }
    def load_from_env(self):
        env_mode = os.getenv('APP_MODE')
        if env_mode and env_mode in ['debug', 'production']:
            self.config['mode'] = env_mode
        env_log = os.getenv('LOG_LEVEL')
        if env_log and env_log.upper() in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
            self.config['log_level'] = env_log.upper()
    def get(self, key):
        return self.config.get(key)
if __name__ == '__main__':
    manager = ConfigManager()
    manager.load_from_env()
    print(f"Operational Mode: {manager.get('mode')}")
    print(f"Log Level: {manager.get('log_level')}")