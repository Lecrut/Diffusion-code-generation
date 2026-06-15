def manage_user_settings():
    settings = {
        "theme": "dark",
        "font_size": 12,
        "notifications_enabled": True,
        "language": "en"
    }
    def update_setting(key, value):
        if key in settings:
            current_value = settings[key]
            if isinstance(value, type(current_value)):
                settings[key] = value
            else:
                print(f"Error: Type mismatch for setting '{key}'. Expected {type(current_value).__name__}, got {type(value).__name__}.")
        else:
            print(f"Error: Setting '{key}' not found.")
    def get_setting(key):
        if key in settings:
            return settings[key]
        else:
            return None
    return update_setting, get_setting, settings
if __name__ == '__main__':
    update, get, current_settings = manage_user_settings()
    print("--- Initial Settings ---")
    print(current_settings)
    print("\n--- Retrieving Settings ---")
    theme = get("theme")
    font_size = get("font_size")
    notifications = get("notifications_enabled")
    print(f"Theme: {theme}")
    print(f"Font Size: {font_size}")
    print(f"Notifications Enabled: {notifications}")
    print("\n--- Updating Settings ---")
    update("theme", "light")
    update("font_size", 14)
    update("notifications_enabled", False)
    update("non_existent_key", "test")
    print("\n--- Final Settings ---")
    print(current_settings)
    print("\n--- Verifying Updates ---")
    theme = get("theme")
    font_size = get("font_size")
    notifications = get("notifications_enabled")
    print(f"New Theme: {theme}")
    print(f"New Font Size: {font_size}")
    print(f"New Notifications Enabled: {notifications}")