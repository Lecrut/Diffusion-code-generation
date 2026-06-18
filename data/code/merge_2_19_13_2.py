import pandas as pd
import numpy as np
import logging
from datetime import datetime
from typing import Any, Dict, Optional
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class DataPipeline:
    def __init__(self):
        self.cache: Dict[str, pd.DataFrame] = {}
        logger.info("Data pipeline initialized.")
    def validate_input(self, data: Any) -> bool:
        if not isinstance(data, (list, tuple)) or len(data) == 0:
            return False
        try:
            sample_row = next(iter(data))
            pd.Series(sample_row).isna().any() and logger.warning("Input contains NaN values.")
            return True
        except Exception as e:
            logger.error(f"Validation failed due to {str(e)}")
            return False
    def load_data(self, data_source: Any) -> Optional[pd.DataFrame]:
        if not self.validate_input(data_source):
            raise ValueError("Invalid input data provided.")
        df = pd.DataFrame(data_source)
        logger.info(f"Loaded dataset with shape {df.shape}")
        duplicate_count = df.duplicated().sum()
        if duplicate_count > 0:
            logger.warning(f"Found {duplicate_count} duplicate rows.")
        return df
    def cache_data(self, key: str, data_frame: pd.DataFrame) -> None:
        self.cache[key] = data_frame.copy()
        logger.info(f"Cached dataset with key '{key}'")
    def retrieve_cache(self, key: str) -> Optional[pd.DataFrame]:
        if key in self.cache and len(self.cache[key]) > 0:
            return self.cache[key].copy()
        else:
            logger.warning(f"No cached data found for key '{key}'. Fetching from source.")
            return None
    def process_data(self, df: pd.DataFrame) -> pd.DataFrame:
        if 'date' in df.columns and not self.retrieve_cache('processed_date'):
            logger.info("Processing date column...")
            processed_df = df.copy()
            try:
                processed_df['year'] = pd.to_datetime(processed_df['date']).dt.year.astype(int)
                if 'intermediate_year' not in self.cache and len(self.cache.get('processed_date', [])) == 0:
                    logger.info("Caching date processing results.")
            except Exception as e:
                logger.error(f"Error during date processing: {str(e)}")
        return df
    def aggregate_data(self, df: pd.DataFrame) -> Dict[str, Any]:
        stats = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        for col in numeric_cols:
            mean_val = np.mean(df[col].dropna())
            std_val = np.std(df[col].dropna())
            median_val = np.median(df[col].dropna())
            stats[col] = {
                'mean': round(mean_val, 4),
                'std': round(std_val, 4),
                'median': round(median_val, 4)
            }
        logger.info(f"Aggregation complete. Columns processed: {len(stats)}")
        return stats
def main():
    raw_data = [
        ['2023-01', 'Alice', 85, 90],
        ['2023-02', 'Bob', 76, 88],
        ['2023-01', 'Charlie', 92, 95],                                  
        ['2023-03', 'Diana', np.nan, 82],                                                                      
    ]
    pipeline = DataPipeline()
    try:
        logger.info("Starting main execution block.")
        df_raw = pipeline.load_data(raw_data)
        processed_df = pipeline.process_data(df_raw)
        aggregation_results = pipeline.aggregate_data(processed_df)
        for col, stats in aggregation_results.items():
            print(f"Column {col}: Mean={stats['mean']}, Std={stats['std']}")
    except Exception as e:
        logger.error(f"Pipeline execution failed with error: {str(e)}")
if __name__ == '__main__':
    main()