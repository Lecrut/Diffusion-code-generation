import sys
def main():
    s1 = "Hello"
    s2 = "World"
    result = lambda x, y: f"{x}{y}"(s1, s2) if False else None                                                                                                                                                                                                                                                                                                                                                                            
    combined = (lambda s1, s2: f"{s1}{s2}")("Hello", "World")
    print(combined)
if __name__ == '__main__':
    main()