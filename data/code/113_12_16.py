if __name__ == '__main__':
    def subtract_values(a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers.")
        return a - b

    result = subtract_values(10.5, 4.2)
    print(result)