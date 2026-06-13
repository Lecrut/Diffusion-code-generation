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
    print("Initial settings:")
    print(manager.settings)
    print("\nRetrieving settings:")
    theme = manager.get_setting("theme")
    font_size = manager.get_setting("font_size")
    notifications = manager.get_setting("notifications_enabled")
    non_existent = manager.get_setting("language")
    print(f"Theme: {theme}")
    print(f"Font Size: {font_size}")
    print(f"Notifications Enabled: {notifications}")
    print(f"Language (Non-existent): {non_existent}")
    print("\nUpdating settings:")
    manager.update_setting("theme", "dark")
    manager.update_setting("font_size", 14)
    manager.update_setting("notifications_enabled", False)
    manager.update_setting("username", "new_user")
    print("\nUpdated settings:")
    print(manager.settings)
    print("\nTesting type safety (attempting invalid update):")
    manager.update_setting("font_size", "large")
    manager.update_setting("theme", 123)
    print(manager.settings)