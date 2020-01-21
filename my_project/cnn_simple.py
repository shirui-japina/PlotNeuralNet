import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),

    # input 
    to_input("/Users/shirui/Desktop/test/aa.png", to='(-2.5,0,0)', width=9, height=9, name='temp'),

    to_Conv("c1", 44, 20, offset="(0,0,0)", height=40, depth=40, width=2, caption="conv1"),
    to_Pool("p1", offset="(0.4,0,0)", to="(0,0,0)", height=35, depth=35, width=2, opacity=0.5, caption=""),

    to_Conv("c2", 16, 50, offset="(2.6,0,0)", height=30, depth=30, width=4, caption="conv2"),
    to_connection("p1", "c2"),
    to_Pool("p2", offset="(3.4,0,0)", to="(0,0,0)", height=25, depth=25, width=4, opacity=0.5, caption=""),

    to_Conv("c3", 2, 500, offset="(5.8,0,0)", height=20, depth=20, width=6, caption="conv3"),
    to_connection("p2", "c3"),
    to_Pool("p3", offset="(7,0,0)", to="(0,0,0)", height=15, depth=15, width=6, opacity=0.5, caption=""),

    to_UnPool("Dropout", offset="(9.7,0,0)", to="(0,0,0)", height=15, depth=15, width=6, opacity=0.5, caption="Dropout"),
    to_connection("p3", "Dropout"),
    to_Conv("c4", 1, 2, offset="(12.4,0,0)", height=8, depth=8, width=3, caption="conv4"),
    to_connection("Dropout", "c4"),

    to_SoftMax("SoftMax", s_filer=2, offset="(14,0,0)", to="(0,0,0)", width=3, height=3, depth=6, opacity=0.7, caption="SoftMax"),
    to_connection("c4", "SoftMax"),

    to_end(),
]
def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
