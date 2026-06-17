class FigureAnalyzer:
    def find_range(self, figures):
        if not figures:
            return None
        return (min(figures), max(figures))
if __name__ == '__main__':
    analyzer = FigureAnalyzer()
    sample_figures1 = [10, 5, 20, 15]
    result1 = analyzer.find_range(sample_figures1)
    print(f"Range for {sample_figures1}: {result1}")
    sample_figures2 = [-5, 100, 0, -10]
    result2 = analyzer.find_range(sample_figures2)
    print(f"Range for {sample_figures2}: {result2}")
    sample_figures3 = [42]
    result3 = analyzer.find_range(sample_figures3)
    print(f"Range for {sample_figures3}: {result3}")
    sample_figures4 = []
    result4 = analyzer.find_range(sample_figures4)
    print(f"Range for {sample_figures4}: {result4}")