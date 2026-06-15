class FigureAnalyzer:
    def find_range(self, figures):
        if not figures:
            return None
        return (min(figures), max(figures))
if __name__ == '__main__':
    analyzer = FigureAnalyzer()
    sample_figures1 = [10, 5, 20, 15]
    sample_figures2 = [3.14, 1.618, 2.718]
    sample_figures3 = []
    sample_figures4 = [100]
    range1 = analyzer.find_range(sample_figures1)
    print(f"Range for {sample_figures1}: {range1}")
    range2 = analyzer.find_range(sample_figures2)
    print(f"Range for {sample_figures2}: {range2}")
    range3 = analyzer.find_range(sample_figures3)
    print(f"Range for {sample_figures3}: {range3}")
    range4 = analyzer.find_range(sample_figures4)
    print(f"Range for {sample_figures4}: {range4}")