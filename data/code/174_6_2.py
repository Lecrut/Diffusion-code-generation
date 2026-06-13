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
                raise TypeError(f"Value for {key} must be of type {type(current_value).__name__}, got {type(value).__name__}")
        else:
            raise KeyError(f"Setting '{key}' not found")
    def get_setting(key):
        if key in settings:
            return settings[key]
        else:
            raise KeyError(f"Setting '{key}' not found")
    return settings, update_setting, get_setting
if __name__ == '__main__':
    user_settings, update, get = manage_user_settings()
    print("Initial Settings:")
    print(user_settings)
    try:
        new_theme = "light"
        update("theme", new_theme)
        print("\nAfter updating theme:")
        print(user_settings)
        new_font_size = 14
        update("font_size", new_font_size)
        print("\nAfter updating font_size:")
        print(user_settings)
        new_notifications = False
        update("notifications_enabled", new_notifications)
        print("\nAfter updating notifications_enabled:")
        print(user_settings)
        print("\nRetrieving specific settings:")
        theme = get("theme")
        font_size = get("font_size")
        notifications = get("notifications_enabled")
        print(f"Theme: {theme}")
        print(f"Font Size: {font_size}")
        print(f"Notifications Enabled: {notifications}")
        print("\nAttempting invalid update (Type Error expected):")
        try:
            update("font_size", "large")
        except TypeError as e:
            print(f"Caught expected error: {e}")
        print("\nAttempting to retrieve non-existent setting (KeyError expected):")
        try:
            get("non_existent_key")
        except KeyError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")