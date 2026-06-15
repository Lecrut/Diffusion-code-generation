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
                if isinstance(current_value, int) and isinstance(value, int):
                    self.settings[key] = value
                elif isinstance(current_value, bool) and isinstance(value, bool):
                    self.settings[key] = value
                else:
                    raise TypeError(f"Cannot update setting '{key}' from type {type(value)} to incompatible type.")
        else:
            raise KeyError(f"Setting '{key}' not found.")
    def get_setting(self, key):
        if key in self.settings:
            return self.settings[key]
        else:
            raise KeyError(f"Setting '{key}' not found.")
if __name__ == '__main__':
    manager = SettingsManager()
    print("--- Initial Settings ---")
    print(manager.settings)
    try:
        print("\n--- Retrieving Settings ---")
        theme = manager.get_setting("theme")
        font_size = manager.get_setting("font_size")
        notifications = manager.get_setting("notifications_enabled")
        print(f"Theme: {theme} (Type: {type(theme)})")
        print(f"Font Size: {font_size} (Type: {type(font_size)})")
        print(f"Notifications Enabled: {notifications} (Type: {type(notifications)})")
        print("\n--- Updating Settings ---")
        manager.update_setting("theme", "dark")
        manager.update_setting("font_size", 14)
        manager.update_setting("notifications_enabled", False)
        manager.update_setting("username", "new_user_name")
        print("\n--- Updated Settings ---")
        print(manager.settings)
        print("\n--- Testing Error Handling (KeyError) ---")
        try:
            manager.get_setting("non_existent_key")
        except KeyError as e:
            print(f"Caught expected error: {e}")
        print("\n--- Testing Error Handling (TypeError during update) ---")
        try:
            manager.update_setting("font_size", "large")
        except TypeError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")