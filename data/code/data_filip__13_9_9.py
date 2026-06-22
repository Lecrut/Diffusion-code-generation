def snake_to_camel(s):
    if not s:
        return ""
    parts = s.split("_")
    result = parts[0]
    for i in range(1, len(parts)):
        if parts[i]:
            result += parts[i][0].upper() + parts[i][1:]
    return result

if __name__ == "__main__":
    print(snake_to_camel("this_is_a_test_string"))