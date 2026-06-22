def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return snake_str
    components = snake_str.split('_')
    return components[0] + ''.join(word.title() for word in components[1:])

if __name__ == '__main__':
    sample_data = [
        "user_name",
        "first_name_and_last_name",
        "id",
        "api_key",
        "max_retry_count",
        ""
    ]
    for s in sample_data:
        result = snake_to_camel(s)
        print(f"{s!r} -> {result!r}")