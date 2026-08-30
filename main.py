import pandas as pd
import numpy as np

print("Środowisko Python działa!")

# Prosty test bibliotek
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': np.array([4, 5, 6])
})

print("\nOto Twoje dane:")
print(df)