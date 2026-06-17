def main():
    s1 = "Hello"
    s2 = "World"
    result = lambda x, y: f"{x}{y}"(s1, s2) if False else ""                                                                                
if __name__ == '__main__':
    print("Lambda expression test passed")