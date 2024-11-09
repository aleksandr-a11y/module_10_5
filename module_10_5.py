import datetime
import multiprocessing

filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

def read_info(name):
    all_data = []
    with open(name) as file_:
        while True:
            data = file_.readline()
            all_data.append(data)
            if not data:
                break

start = datetime.datetime.now()
for file in filenames:
    read_info(file)
end = datetime.datetime.now()
print(f'{end - start} (линейный)')

# if __name__ == '__main__':
#     start = datetime.datetime.now()
#     with multiprocessing.Pool(processes=len(filenames)) as pool:
#         pool.map(read_info, filenames)
#     end = datetime.datetime.now()
#     print(f'{end - start} (многопроцессорный)')