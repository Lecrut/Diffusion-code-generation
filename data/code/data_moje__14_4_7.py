def get_third_item() -> str:
    items: list[str] = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    return items[2]

if __name__ == '__main__':
    result: str = get_third_item()
    print(result)