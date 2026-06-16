import os
class ConfigManager:
    def __init__(self):
        self.config = {
            'mode': 'default',
            'debug': False,
            'log_level': 'INFO'
        }
    def load_from_env(self):
        env_mode = os.getenv('APP_MODE')
        if env_mode:
            self.config['mode'] = env_mode.lower()
        debug_str = os.getenv('DEBUG', '').lower()
        self.config['debug'] = debug_str in ('true', '1', 'yes')
    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read().strip()
            if not content.startswith('#'):
                parts = content.split(',')
                for part in parts:
                    key_val = part.strip().split('=')
                    if len(key_val) == 2:
                        k, v = key_val[0].strip(), key_val[1].strip()
                        self.config[k.lower()] = v
        except FileNotFoundError:
            pass
def get_mode(config):
    return config['mode']
if __name__ == '__main__':
    manager = ConfigManager()
    sample_config_file_path = 'config_sample.txt'
    if os.path.exists(sample_config_file_path):
        manager.load_from_file(sample_config_file_path)
    manager.load_from_env()
    current_mode = get_mode(manager.config)
    print(f"Operational Mode: {current_mode}")