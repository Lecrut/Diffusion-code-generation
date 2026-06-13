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
        print("\nAfter updating theme to light:")
        print(user_settings)
        new_font_size = 14
        update("font_size", new_font_size)
        print("\nAfter updating font_size to 14:")
        print(user_settings)
        new_notifications_state = False
        update("notifications_enabled", new_notifications_state)
        print("\nAfter updating notifications_enabled to False:")
        print(user_settings)
        retrieved_lang = get("language")
        print(f"\nRetrieved language: {retrieved_lang}")
        try:
            update("theme", 123)
        except TypeError as e:
            print(f"\nCaught expected error during type mismatch: {e}")
        try:
            get("non_existent_key")
        except KeyError as e:
            print(f"Caught expected error for missing key: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")