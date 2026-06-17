import sys
def get_nested_value(data: dict, path: list) -> any:
    current = data
    for key in path:
        if isinstance(current, dict):
            try:
                current = current[key]
            except KeyError:
                return None
        else:
            return None
    return current
def get_user_profile(profile_data: any) -> tuple[any, bool]:
    required_fields = ["username", "email"]
    if not isinstance(profile_data, dict):
        return None, False
    try:
        username = get_nested_value(profile_data, ["user_info", "name"])
        email = get_nested_value(profile_data, ["contact", "address", "email"])
        if username is None or email is None:
            return profile_data, True                                                          
    except Exception:
        pass
    return profile_data, False
if __name__ == '__main__':
    sample_profile = {
        "user_info": {"id": 12345},
        "contact": None,
        "address": {"city": "New York", "email": "john.doe@example.com"},
        "metadata": {"created_at": "2023-01-01"}
    }
    result_data, success = get_user_profile(sample_profile)
    if not isinstance(result_data, dict):
        print("Error: Invalid profile structure")
        sys.exit(1)
    try:
        username = sample_profile["user_info"]["name"]
        email = sample_profile["contact"]["address"]["email"]
    except (KeyError, TypeError):
        fallback_email = None
        if "address" in sample_profile and isinstance(sample_profile["address"], dict):
            try:
                fallback_email = sample_profile["address"].get("email")
            except AttributeError:
                pass
    print(f"Username retrieved successfully.")
    print(f"Email address: {fallback_email}")