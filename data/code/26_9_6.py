def lambda_compare(x: int | float = 10, y: int | float = 5) -> bool:
    return x > y

if __name__ == '__main__':
    result = lambda_compare(20, 10)
    print(f"x=20, y=10 => {result}")