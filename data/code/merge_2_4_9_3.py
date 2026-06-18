import os
class ConfigManager:
    def __init__(self):
        self.config = {
            'mode': 'default',
            'debug_level': 0,
            'log_file': None
        }
    def load_from_env(self):
        env_mode = os.getenv('APP_MODE')
        if env_mode:
            valid_modes = ['development', 'production', 'maintenance']
            self.config['mode'] = env_mode.lower() if env_mode in valid_modes else 'default'
        debug_str = os.getenv('DEBUG_LEVEL', '0')
        try:
            self.config['debug_level'] = int(debug_str)
        except ValueError:
            pass
    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read().strip()
                if not content.startswith('#'):
                    lines = [line.strip() for line in content.split('\n')]
                    self.config['mode'] = next((l for l in lines if '=' in l), self.config['mode'])
        except FileNotFoundError:
            pass
    def get_mode(self):
        return self.config.get('mode', 'default')
if __name__ == '__main__':
    manager = ConfigManager()
    manager.load_from_env()
    print(f"Operational Mode: {manager.get_mode()}")