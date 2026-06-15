class SettingsManager:
    def __init__(self):
        self.settings = {
            "theme": "light",
            "font_size": 12,
            "notifications_enabled": True,
            "username": "default_user"
        }
    def update_setting(self, key, value):
        if key in self.settings:
            current_value = self.settings[key]
            if isinstance(value, type(current_value)):
                self.settings[key] = value
            else:
                print(f"Error: Type mismatch for setting '{key}'. Expected {type(current_value).__name__}, got {type(value).__name__}.")
        else:
            print(f"Error: Setting '{key}' not found.")
    def get_setting(self, key):
        if key in self.settings:
            return self.settings[key]
        else:
            return None
if __name__ == '__main__':
    manager = SettingsManager()
    print("--- Initial Settings ---")
    print(f"Theme: {manager.get_setting('theme')} (Type: {type(manager.get_setting('theme'))})")
    print(f"Font Size: {manager.get_setting('font_size')} (Type: {type(manager.get_setting('font_size'))})")
    print(f"Notifications Enabled: {manager.get_setting('notifications_enabled')} (Type: {type(manager.get_setting('notifications_enabled'))})")
    print(f"Username: {manager.get_setting('username')}")
    print("\n--- Updating Settings ---")
    manager.update_setting("theme", "dark")
    manager.update_setting("font_size", 14)
    manager.update_setting("notifications_enabled", False)
    manager.update_setting("non_existent_key", "test")
    print("\n--- Updated Settings ---")
    print(f"Theme: {manager.get_setting('theme')} (Type: {type(manager.get_setting('theme'))})")
    print(f"Font Size: {manager.get_setting('font_size')} (Type: {type(manager.get_setting('font_size'))})")
    print(f"Notifications Enabled: {manager.get_setting('notifications_enabled')} (Type: {type(manager.get_setting('notifications_enabled'))})")
    print(f"Username: {manager.get_setting('username')}")