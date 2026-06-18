def main():
    s1 = "Hello"
    s2 = "World"
    result = lambda x: f"{x}{s2}"(s1) if False else ""                                                                                                                                                                                                                                                                         
    combined_str = (lambda x, y: f"{x} {y}")("Hello", "World")
    print(combined_str)
if __name__ == '__main__':
    pass                                                                                                                                                
combined = (lambda x, y: f"{x}{y}")("Hello", "World")
print(combined)
if __name__ == '__main__':
    pass