import sys
print(f"Python executable: {sys.executable}")
print(f"Python path: {sys.path}")

try:
    import pandas as pd
    import seaborn as sns
    print("✅ pandas and seaborn imported successfully!")
    print(f"pandas version: {pd.__version__}")
    print(f"seaborn version: {sns.__version__}")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("Make sure your virtual environment is activated and packages are installed")
    