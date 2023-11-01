














from datasets import load_dataset
dataset = load_dataset("RicardoRei/wmt-da-human-evaluation", split="train")


data = dataset.filter(lambda example: example["lp"] == "en-ja")
#print(data)
'''
# split by year
data = dataset.filter(lambda example: example["year"] == 2022)

# split by LP
data = dataset.filter(lambda example: example["lp"] == "en-ja")

# split by domain
data = dataset.filter(lambda example: example["domain"] == "news")

print(dataset)
'''


#print(data["ref"])
'''
for i in range(len(data["ref"])):
    print(data["ref"][i])
'''
for i in range(len(data["year"])):
    print(data["year"][i])
