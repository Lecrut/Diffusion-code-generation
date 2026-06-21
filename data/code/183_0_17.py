def strip_names(names_str):
    if not isinstance(names_str, str) or ',' not in names_str:
        raise ValueError("Input must be a string containing comma-separated names.")
    return [name.strip() for name in names_str.split(',')]

if __name__ == '__main__':
    sample_names = "  Alice, Bob , Charlie "
    try:
        result = strip_names(sample_names)
        print(result)
    except ValueError as e:
        print(e)