import pandas as pd
import numpy as np
import logging
from datetime import datetime
from typing import Dict, Any, Tuple, Optional
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class DataPipeline:
    def __init__(self):
        self.cache: Dict[str, pd.DataFrame] = {}
    def validate_input(self, data: Any) -> Tuple[bool, str]:
        if not isinstance(data, (pd.Series, pd.DataFrame)):
            return False, "Input must be a pandas Series or DataFrame"
        try:
            numeric_cols = [col for col in data.select_dtypes(include=[np.number]).columns]
            categorical_cols = [col for col in data.select_dtypes(exclude=[np.number]).columns]
            if not numeric_cols and not categorical_cols:
                return False, "Data must contain at least one column"
        except Exception as e:
            logger.error(f"Validation error during type checking: {e}")
            return False, f"Invalid data structure detected: {str(e)}"
        return True, ""
    def load_sample_data(self) -> pd.DataFrame:
        logger.info("Loading hardcoded sample data...")
        raw_data = [
            {'id': 101, 'name': 'Alice', 'score': 85.5},
            {'id': 102, 'name': 'Bob', 'score': 92.3},
            {'id': 103, 'name': 'Charlie', 'score': 78.9},
        ]
        df = pd.DataFrame(raw_data)
        logger.debug(f"Loaded sample data with shape: {df.shape}")
        return df
    def process_intermediate(self, current_df: pd.DataFrame) -> pd.DataFrame:
        cache_key = f"{current_df.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        if not self.cache.get(cache_key):
            logger.info("Processing new dataset...")
            current_df['score_normalized'] = (current_df['score'] - 50) / 42.7
            if cache_key not in self.cache:
                logger.debug("Caching intermediate results...")
        else:
            logger.info(f"Retrieving cached data from {cache_key}")
        return current_df.copy()
    def run_pipeline(self) -> pd.DataFrame:
        try:
            raw_data = self.load_sample_data()
            is_valid, validation_msg = self.validate_input(raw_data)
            if not is_valid or validation_msg:
                logger.error(f"Pipeline aborted due to invalid input: {validation_msg}")
                raise ValueError(validation_msg)
            processed_df = self.process_intermediate(raw_data.copy())
            final_stats = processed_df.groupby('name').agg({
                'score': ['mean', 'max'], 
                'id': 'count'
            }).reset_index()
            logger.info(f"Pipeline completed successfully. Output shape: {final_stats.shape}")
            return final_stats
        except Exception as e:
            logger.critical(f"FATAL ERROR in pipeline execution: {e}", exc_info=True)
            raise
if __name__ == '__main__':
    try:
        pipeline = DataPipeline()
        result_df = pipeline.run_pipeline()
        if not isinstance(result_df, pd.DataFrame):
            logger.error("Expected DataFrame output but got something else")
        print("\n--- Final Analysis Results ---")
        print(result_df.to_string(index=False))
    except Exception as e:
        pass