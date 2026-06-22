def yards_to_kilometers(yards):
    if not isinstance(yards, (int, float)):
        raise ValueError("Input must be a number")
    return yards * 0.0254

if __name__ == '__main__':
    print(yards_to_kilometers(10))
    print(yards_to_kilometers(100))