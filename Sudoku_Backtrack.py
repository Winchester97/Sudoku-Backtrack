# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:39:02 2020

@author: Rizky Dewa Sakti_1301180358
"""

#input soal sudoku
Board = [
    [4,0,0,8,0,0,5,7,0],        
    [0,5,0,0,2,0,0,1,0],
    [9,0,0,0,0,5,6,0,0],
    [7,0,0,0,0,0,0,5,0],
    [0,9,6,0,0,0,3,2,0],
    [0,4,0,0,0,0,0,0,6],
    [0,0,4,1,0,0,0,0,9],
    [0,7,0,0,8,0,0,3,0],
    [0,2,8,0,0,9,0,0,5],        
]

def print_board(B):
    
    for i in range(len(B)):
        if ( i % 3 == 0 ) and (i != 0):
            print('- - - - - - - - - - - - - - -')
            
        for j in range(len(B[i])):
            if (j % 3 == 0) and (j != 0):
                print(' | ', end="")
                
            if (j != 8):
                print (str(B[i][j]) + " ", end="")
                
            else: 
                print (B[i][j])


                
def find_empty(B):
    for i in range(len(B)):
        for j in range(len(B[i])):
            if (B[i][j] == 0):
                return i,j #Baris, Kolom
    return None
        
def valid(B, num, pos):
    #Cek Baris
    for i in range(len(B[0])):
        if B[pos[0]][i] == num and pos[1] != i:
            return False
        
    #Cek Kolom
    for i in range(len(B[0])):
        if B[i][pos[1]] == num and pos[0] != i:
            return False
    #Cek Box
    box_x = pos[0] // 3  
    box_y = pos[1] // 3
    #pos [0] dn pos[1] = [0,2,..,8]
    #pos[0] dan pos[1] div 3 kqrena akan dikonversi menjadi bagian box[0,1,2] -->   #    7 8 0  | 4 0 0  | 1 2 0
                                                                                    #    6 0 0  | 0 7 5  | 0 0 9
                                                                                    #    0 0 0  | 6 0 1  | 0 7 8
                                                                                    #   box_x=0   box_x=1  box_x=2
                                                                                    #   box_y=0   box_y=0  box_y=0 
                                                                                    #    - - - - - - - - - - - - 
                                                                                    #    0 0 7  | 0 4 0  | 2 6 0
                                                                                    #    0 0 1  | 0 5 0  | 9 3 0
                                                                                    #    9 0 4  | 0 6 0  | 0 0 5
                                                                                    #   box_x=0
                                                                                    #   box_y=1   
                                                                                    #    - - - - - - - - - - - - 
                                                                                    #    0 7 0  | 3 0 0  | 0 1 2
                                                                                    #    1 2 0  | 0 0 7  | 4 0 0
                                                                                    #    0 4 9  | 2 0 6  | 0 0 7
                                                                                    #   box_x=0
                                                                                    #   box_y=2 

    for i in range(box_x * 3, box_x*3 + 3): 
    #ex: pos[0] = 7, so box_x = 2, then iterate i in range (6,9)
        for j in range(box_y * 3, box_y*3 + 3): 
        #ex: pos[1] = 5, so box_y = 1, then iterate i in range (3,6)
        
    #dari contoh diatas, kita mendapatkan box_x=2, box_y=1 jadi kita mengece box 2,1 --># |2 6 0|
                                                                                        # |9 3 0|
                                                                                        # |0 0 5|
            if (B[i][j] == num)  and ((i,j) != pos): 
            # (B[i][j] == num) untuk mengecek tidak ada num yg sama di suatu box
            # ((i,j) != pos) untuk memastikan (i,j) tidak mengulang mengecek posisi yg sama dengan input (pos)
                return False
    
    return True
def sudoku_backtrack(B):
    #Base Case
    find = find_empty(B)
    if not find:
        return True #return true jika semua row,col telah diisi
    else:
        row, col = find

    for i in range(1,10): #Mengisi baris,kolom dengan angka 1,2,..,9
        if valid(B, i, (row, col)): #cek apakah num baru yaitu: i, valid untuk diinput ke Board
            B[row][col] = i

            if sudoku_backtrack(B): #pendekatan rekursif sampai kita menemukan solusi atau saat input 1..9 tidak ada yang valid.
                return True
            
                # Saat input 1..9 tidak ada yg valid:
                # maka akan return false (di baris 115) dan menyebabkan line (104) tidak dikerjakan
                # lalu, baris (112) akan mereset row,col yang barus kita inputkan dan mengulanginya lagi dengan menginput num baru yaitu: i
                # di baris 101 melalui pendekatan reksursif di baris (104)

            B[row][col] = 0 #saat input 1..9 tidak ada yang valid, maka akan mereset angka di baris,kolom tsb 
            # dan melakukan backtrack di pendekatan rekursif tadi

    return False

print("")
print("--------------Board Awal--------------")    
print("")    
print_board(Board)
sudoku_backtrack(Board)
print("")
print("--------------HASIL-------------------")
print("")
print_board(Board)                