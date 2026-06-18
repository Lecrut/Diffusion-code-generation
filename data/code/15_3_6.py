def same_value(x: int = 10, y: int = 20) -> bool:
    return x == y if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    print(same_value(5, 5), "should be True")