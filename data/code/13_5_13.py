def to_camel_case(snake_str: str) -> str:
    return "".join(word if i == 0 else word.capitalize() for i, word in enumerate(snake_str.split("_")))

if __name__ == "__main__":
    sample_input = "hello_world_example"
    result = to_camel_case(sample_input)
    print(result)