def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split("_")
    if not components:
        return ""
    return components[0] + "".join(word.capitalize() for word in components[1:])

if __name__ == "__main__":
    sample = "hello_world_example"
    print(snake_to_camel(sample))