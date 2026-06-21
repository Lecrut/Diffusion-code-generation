def evaluate_access_control(user_permissions):
    rules = {
        "can_edit": (user_permissions.get("role") == "admin" and user_permissions.get("verified")),
        "can_view": (user_permissions.get("role") in ["admin", "editor"]),
        "can_delete": (user_permissions.get("role") == "admin"),
        "can_share": (user_permissions.get("permissions").get("share", False) and user_permissions.get("owner"))
    }
    return rules

if __name__ == '__main__':
    sample_user_permissions = {
        "role": "editor",
        "verified": True,
        "permissions": {
            "share": True
        },
        "owner": True
    }
    access_control_results = evaluate_access_control(sample_user_permissions)
    print(access_control_results)