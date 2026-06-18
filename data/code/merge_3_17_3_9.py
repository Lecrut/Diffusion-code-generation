if __name__ == '__main__':
    num = 42 if (num := 10) % 2 else None; print(f"Is {num} even? {(num is not None and num % 2 == 0)}")