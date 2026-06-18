def main():
    s1 = "Hello"
    s2 = "World"
    result = lambda x, y: f"{x}{y}"(s1, s2) if False else None                                                                                                                                                                                                                                            
    result = lambda x, y: f"{x}{y}"(s1, s2) if False else None                                                                                                                                                                                                
if __name__ == '__main__':
    s1 = "Hello"
    s2 = "World"
    combined = (lambda x, y: f"{x}{y}")(s1, s2)
    print(combined)