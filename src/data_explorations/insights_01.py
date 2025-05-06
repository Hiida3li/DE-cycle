import json
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

with open("gulf_chats_merged.json", "r") as f:
    data = json.load(f)

# Extract topics from chat_id
topics = [chat["chat_id"].rsplit("_", 1)[0].strip() for chat in data]

# Count occurrences of each topic
topic_counts = Counter(topics)

# Print topic counts (optional)
for topic, count in topic_counts.items():
    print(f"{topic}: {count}")

# Plot the distribution
plt.figure(figsize=(10, 6))
plt.bar(topic_counts.keys(), topic_counts.values(), color="mediumpurple")
plt.xticks(rotation=45, ha="right")
plt.title("Number of Conversations per Topic")
plt.xlabel("Topic")
plt.ylabel("Number of Conversations")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
