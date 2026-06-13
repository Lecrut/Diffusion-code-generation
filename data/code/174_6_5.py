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
        new_notifications_status = False
        update("notifications_enabled", new_notifications_status)
        print("\nAfter updating notifications_enabled:")
        print(user_settings)
        print("\nRetrieving specific settings:")
        theme = get("theme")
        font_size = get("font_size")
        notifications = get("notifications_enabled")
        language = get("language")
        print(f"Theme: {theme} (Type: {type(theme).__name__})")
        print(f"Font Size: {font_size} (Type: {type(font_size).__name__})")
        print(f"Notifications Enabled: {notifications} (Type: {type(notifications).__name__})")
        print(f"Language: {language} (Type: {type(language).__name__})")
    except (KeyError, TypeError) as e:
        print(f"\nAn error occurred: {e}")