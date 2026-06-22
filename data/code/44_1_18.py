class ScoreAnalyzer:
    EMPTY_RETURN_VALUE = 0.0
    
    @staticmethod
    def _validate_scores(scores):
        if scores is None:
            raise ValueError("Scores cannot be None")
        if len(scores) == 0:
            return ScoreAnalyzer.EMPTY_RETURN_VALUE
        return scores
    
    def compute_mean(self, scores):
        validated_scores = self._validate_scores(scores)
        if isinstance(validated_scores, float):
            return validated_scores
        
        total = 0.0
        count = len(scores)
        for score in scores:
            total += float(score)
        
        if count == 0:
            return ScoreAnalyzer.EMPTY_RETURN_VALUE
        
        return total / count

if __name__ == '__main__':
    analyzer = ScoreAnalyzer()
    test_scores = [85, 92, 78, 90, 88]
    mean_result = analyzer.compute_mean(test_scores)
    print(mean_result)