import os
class ConfigManager:
    def __init__(self):
        self.config = {
            "debug": False,
            "verbose": True,
            "output_format": "json",
            "log_level": "INFO"
        }
    def load_from_env(self):
        if os.getenv("DEBUG"):
            self.config["debug"] = True
        if os.getenv("VERBOSE") == "1":
            self.config["verbose"] = True
        mode = os.getenv("OUTPUT_FORMAT", "").upper() or None
        valid_formats = ["JSON", "TEXT", "CSV"]
        if mode in valid_formats:
            self.config["output_format"] = mode.lower()
    def load_from_file(self, filepath):
        try:
            with open(filepath, 'r') as f:
                content = f.read().strip()
                key_value_pairs = [line.split('=') for line in content if '=' in line]
                self.config.update({kv[0].lower(): kv[1].lower() for kv in key_value_pairs})
        except FileNotFoundError:
            pass
    def get_mode(self):
        return "DEBUG" if self.config["debug"] else ("VERBOSE" if self.config["verbose"] else "NORMAL")
if __name__ == '__main__':
    manager = ConfigManager()
    env_file_path = os.getenv("CONFIG_FILE", None)
    if env_file_path:
        try:
            with open(env_file_path, 'r') as f:
                for line in f:
                    key_value_pairs = [line.strip().split('=')]
                    manager.config.update({kv[0].lower(): kv[1]})
        except FileNotFoundError:
            pass
    mode = manager.get_mode()
    print(f"Operational Mode: {mode}")