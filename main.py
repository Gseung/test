# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import torch as pt
import itertools

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class test:
    def __init__(self):
        self.numbers = [n for n in range(1, 11)]

    def __getitem__(self, idx):
         return self.numbers[idx]


a = test()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('test')
    print(a.numbers[2:5])
    print(a[2:5])
    list1 = [[10, 20], [30, 40], [50, 60]]
    b = np.array(list1)
    print(b[:, 1])

    default_box = list()
    grids = (38, 19, 10, 5, 3, 1)
    steps = [s / 300 for s in (8, 16, 32, 64, 100, 300)]

    sizes = [s / 300 for s in (30, 60, 111, 162, 213, 264, 315)]
    # print(sizes)

    aspect_ratios = ((2,), (2, 3), (2, 3), (2,), (2,))

    loc_layers = []
    conf_layers = []
    vgg_useful = [21, 33]




    '''
    default_boxes = list()  # 비어있는 리스트 생성
    for k in range(len(grids)):

        for v, u in itertools.product(range(grids[k]), repeat=2):
            cx = (u + 0.5) * steps[k]
            cy = (v + 0.5) * steps[k]

            s = sizes[k]
            default_boxes.append((cx, cy, s, s))

            s = np.sqrt(sizes[k] * sizes[k + 1])
            default_boxes.append((cx, cy, s, s))

            s = sizes[k]
            for ar in aspect_ratios[k]:
                default_boxes.append(
                    (cx, cy, s * np.sqrt(ar), s / np.sqrt(ar)))
                default_boxes.append(
                    (cx, cy, s / np.sqrt(ar), s * np.sqrt(ar)))
                print(f'{cx}, {cy}, {s}, {ar}, {s * np.sqrt(ar)}, {s / np.sqrt(ar)}')


    default_boxes = np.clip(default_boxes, a_min=0, a_max=1)
    default_boxes = np.array(default_boxes)
    '''

    # for i in range(len(grids)):
    #     print(i)

    # print(len(grids))

    # for k in range(len(grids)):
    #     for v, u in itertools.product(range(grids[k]), repeat=2):
    #         print('v')
    #         print(v)
    #         print('u')
    #         print(u)













# See PyCharm help at https://www.jetbrains.com/help/pycharm/
