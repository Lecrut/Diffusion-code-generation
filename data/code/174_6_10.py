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
            raise KeyError(f"Setting '{key}' not found.")
    def get_setting(key):
        if key in settings:
            return settings[key]
        else:
            raise KeyError(f"Setting '{key}' not found.")
    return settings, update_setting, get_setting
if __name__ == '__main__':
    user_settings, update, get = manage_user_settings()
    print("Initial Settings:")
    print(user_settings)
    try:
        print("\nRetrieving 'theme':")
        theme = get("theme")
        print(f"Theme: {theme}, Type: {type(theme)}")
        print("\nRetrieving 'font_size':")
        font_size = get("font_size")
        print(f"Font Size: {font_size}, Type: {type(font_size)}")
        print("\nUpdating 'theme' to 'light':")
        update("theme", "light")
        print(f"New Theme: {get('theme')}")
        print("\nUpdating 'font_size' to 14 (Correct Type):")
        update("font_size", 14)
        print(f"New Font Size: {get('font_size')}")
        try:
            print("\nAttempting to update 'theme' with an incorrect type (int):")
            update("theme", 123)
        except TypeError as e:
            print(f"Caught expected error: {e}")
        try:
            print("\nAttempting to update a non-existent setting:")
            update("non_existent_key", "value")
        except KeyError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    print("\nFinal Settings:")
    print(user_settings)