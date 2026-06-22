def get_third_item() -> str:
    data: list[str] = ["alpha", "beta", "gamma", "delta"]
    return data[2]

if __name__ == '__main__':
    print(get_third_item())