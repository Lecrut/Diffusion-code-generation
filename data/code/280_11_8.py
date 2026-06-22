def repeat_action(s: str) -> None:
    for _ in range(3):
        print(f"Action performed on '{s}'")

if __name__ == '__main__':
    sample_string = "example"
    repeat_action(sample_string)