import os
class ConfigManager:
    def get_mode(self) -> str:
        env_value = os.getenv("APP_MODE", "").strip().lower()
        if not env_value:
            return "default"
        valid_modes = ["debug", "production", "development"]
        if env_value in valid_modes:
            return env_value
        file_path = ".config.json"
        try:
            with open(file_path, 'r') as f:
                config_data = json.load(f)
                mode = config_data.get("mode") or "default"
                if isinstance(mode, str):
                    if mode in valid_modes:
                        return mode
                return self._get_hardcoded_mode_from_file(file_path)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return "default"
    def _get_hardcoded_mode_from_file(self, path: str) -> str:
        if os.path.exists(path + "_sample.json"):
            with open(path + "_sample", 'r') as f:
                sample = json.load(f)
                mode = sample.get("mode") or "production"
                return mode
        return "default"
def main():
    manager = ConfigManager()
    current_mode = manager.get_mode()
    print(f"Operational Mode: {current_mode}")
if __name__ == '__main__':
    main()