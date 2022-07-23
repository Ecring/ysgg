import os
import sys


# 合并并去重
def file_add(file1, file2):
    cache = set()
    with open(file1, "r", encoding="utf-8") as a:
        line = a.readlines()
        data_cache1 = [x.strip() for x in line]
    with open(file2, "r", encoding="utf-8") as a:
        line = a.readlines()
        data_cache2 = [x.strip() for x in line]

    num = len(data_cache1) + len(data_cache2)
    print("正在读取文件...")
    print(f"字典总条目共：{num} 条")
    print("==========================================")
    print(f"开始合并并去重.....")

    for i in data_cache1:
        cache.add(str(i))
    for i in data_cache2:
        cache.add(str(i))
    return cache


# 生成文件
def touch_file():
    if not os.path.exists("./over"):
        os.makedirs("./over")

    with open(f"./over/Over_{f1}+{f2}", "a", encoding="utf-8") as f:
        for i in data:
            f.write(str(i) + "\n")
            print(f"正在重构字典条目：{i}")
        print("==========================================")
        print(f"重构完成！请访问./over/Over_{f1}+{f2}领取您的新字典")


f1 = sys.argv[1]
f2 = sys.argv[2]
data = file_add(f1, f2)
touch_file()