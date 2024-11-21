import pandas as pd
from sklearn.ensemble import IsolationForest

# Load network traffic data
data = pd.read_csv('network_traffic.csv')

# Select relevant features
features = ['src_ip', 'dst_ip', 'protocol', 'bytes_sent', 'bytes_received']
X = data[features]

# Train the Isolation Forest model
model = IsolationForest(contamination=0.1)  # Adjust contamination parameter as needed
model.fit(X)

# Detect anomalies
anomaly_scores = model.decision_function(X)
anomalies = X[anomaly_scores < 0]

# Print anomalies
print("Detected Anomalies:")
print(anomalies)
