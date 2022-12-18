def Fungsi_Print_Main_Menu():
    print('================================================\n')
    print('MAIN MENU PT PURWADHIKA\n')
    print('''List Menu:
    1. Fitur Read
    2. Fitur Create
    3. Fitur Update
    4. Fitur Delete
    5. Exit Program\n''')
def Fungsi_Print_Sub_Menu_1():
    print('================================================\n')
    print('MENU READ DATA\n')
    print('''List Menu:
    1. List karyawan
    2. Detail karyawan
    3. Kembali ke MAIN MENU\n''')
def Fungsi_Print_Sub_Menu_Other(x):
    print('================================================\n')
    print(f'MENU {x.upper()} DATA\n')
    print(f'''List Menu:
    1. {x.title()} karyawan
    2. Kembali ke MAIN MENU\n''')
def Fungsi_Print_Menu_List_Karyawan(): 
    print('Berikut list data karyawan:\n')
    print('ID\t|Nama\t|Age\t|Sex\t|Divisi')
    for i in Dictionary:
        print(Dictionary[i]['ID'],end=('\t|'))
        print(Dictionary[i]['Nama'],end=('\t|'))
        print(Dictionary[i]['Age'],end=('\t|'))
        print(Dictionary[i]['Sex'],end=('\t|'))
        print(Dictionary[i]['Divisi'],end=(''))
        print()
    print()
def Fungsi_Print_Detail_Karyawan(): 
    print('Berikut detail data karyawan:\n')
    print('ID\t: '+Dictionary['ID'+Input_Cari_ID]['ID'])
    print('Nama\t: '+Dictionary['ID'+Input_Cari_ID]['Nama'])
    print('Age\t: '+Dictionary['ID'+Input_Cari_ID]['Age'])
    print('Sex\t: '+Dictionary['ID'+Input_Cari_ID]['Sex'])
    print('Divisi\t: '+Dictionary['ID'+Input_Cari_ID]['Divisi'])
    print()
def Fungsi_Print_Menu_1_Tidak_Ada_Data():
    print('================================================\n')
    print('Tidak ada data yang dapat ditampilkan.\n')
def Fungsi_Print_Format_ID_Salah():
    print('================================================\n')
    print('Format ID yang anda masukan salah. Silahkan masukan ID dengan range dari 001 sampai dengan 999.\n')
def Fungsi_Print_Input_Salah():
    print('================================================\n')
    print('Input yg anda masukan salah.\n')
def Fungsi_Print_Data_Berhasil(x):
    print('================================================\n')
    print(f'{x.title()} data telah berhasil.\n')

ID001={
    'ID':'ID001',
    'Nama':'Alpha',
    'Age':'27',
    'Sex':'L',
    'Divisi':'Operation',
}
ID002={
    'ID':'ID002',
    'Nama':'Beta',
    'Age':'22',
    'Sex':'L',
    'Divisi':'Accounting & Finance',
}
ID003={
    'ID':'ID003',
    'Nama':'Caca',
    'Age':'24',
    'Sex':'P',
    'Divisi':'Marketing',
}
ID004={
    'ID':'ID004',
    'Nama':'Delta',
    'Age':'21',
    'Sex':'L',
    'Divisi':'Human Resources',
}
ID005={
    'ID':'ID005',
    'Nama':'Edna',
    'Age':'25',
    'Sex':'P',
    'Divisi':'IT',
}

Dictionary={'ID001':ID001,'ID002':ID002,'ID003':ID003,'ID004':ID004,'ID005':ID005}
Dictionary_Baru={}

while True:
    Fungsi_Print_Main_Menu()
    Input=str(input('Masukan angka menu yang ingin dijalankan: '))
    print()
    if Input=='1':
        while True:
            Fungsi_Print_Sub_Menu_1()
            Input=str(input('Masukan angka menu yang ingin dijalankan: '))
            print()
            if Input=='1':
                if len(Dictionary)>=1:
                    Fungsi_Print_Menu_List_Karyawan()
                else:
                    Fungsi_Print_Menu_1_Tidak_Ada_Data()
            elif Input=='2':
                if len(Dictionary)>=1:
                    while True:
                        Input_Cari_ID=str(input('Masukan nomor ID yang ingin anda cari (001-999): '))
                        print()
                        if Input_Cari_ID.isnumeric()==True and 0<int(Input_Cari_ID)<1000:
                            if ('ID'+Input_Cari_ID) in Dictionary.keys():
                                Fungsi_Print_Detail_Karyawan()
                                break
                            else:
                                print('================================================\n')
                                print('ID yang anda masukan tidak terdaftar\n')
                                break
                        else:
                            Fungsi_Print_Format_ID_Salah()
                else:
                    Fungsi_Print_Menu_1_Tidak_Ada_Data()
            elif Input=='3':
                break
            else:
                Fungsi_Print_Input_Salah()
    elif Input=='2':
        while True:
            Fungsi_Print_Sub_Menu_Other('create')
            Input=str(input('Masukan angka menu yang ingin dijalankan: '))
            print()
            if Input=='1':
                while True:
                    Input_Cari_ID=str(input('Masukan nomor ID yang ingin anda create (001-999): '))
                    print()
                    if Input_Cari_ID.isnumeric()==True and 0<int(Input_Cari_ID)<1000:
                        if ('ID'+Input_Cari_ID) in Dictionary.keys():
                            print('================================================\n')
                            print('ID yang anda masukan sudah terdaftar\n')
                        else:
                            Create_Nama=str(input('Masukan Nama : '))
                            while True:
                                Create_Age=str(input('Masukan Age : '))
                                if Create_Age.isnumeric()==True:
                                    break
                                else:
                                    print('Age yang anda masukan salah.')
                            while True:
                                Create_Sex=str(input('Masukan Sex (L/P) : '))
                                if Create_Sex.title()=='L' or Create_Sex.title()=='P':
                                    break
                                else:
                                    print('Jenis kelamin yang anda masukan salah.')
                            Create_Division=str(input('Masukan Divisi : '))
                            print()
                            Dictionary_Baru=ID001.copy()
                            Dictionary_Baru['ID']='ID'+Input_Cari_ID
                            Dictionary_Baru['Nama']=Create_Nama.title()
                            Dictionary_Baru['Age']=Create_Age
                            Dictionary_Baru['Sex']=Create_Sex.title()
                            Dictionary_Baru['Divisi']=Create_Division
                            print('Berikut detail data karyawan:\n')
                            print('ID\t: '+Dictionary_Baru['ID'])
                            print('Nama\t: '+Dictionary_Baru['Nama'])
                            print('Age\t: '+Dictionary_Baru['Age'])
                            print('Sex\t: '+Dictionary_Baru['Sex'])
                            print('Divisi\t: '+Dictionary_Baru['Divisi']+'\n')
                            while True:
                                Fitur2_Simpan_Data=str(input('Simpan data? (Y/N) '))
                                print()
                                if Fitur2_Simpan_Data.upper()=='Y':
                                    Dictionary[f'ID{Input_Cari_ID}']=Dictionary_Baru
                                    Fungsi_Print_Data_Berhasil('create')
                                    break
                                elif Fitur2_Simpan_Data.upper()=='N':
                                    break
                            Fungsi_Print_Menu_List_Karyawan()
                        break
                    else:
                        Fungsi_Print_Format_ID_Salah()
            elif Input=='2':
                break
            else:
                Fungsi_Print_Input_Salah()
    elif Input=='3':
        while True:
            Fungsi_Print_Sub_Menu_Other('update')
            Input=str(input('Masukan angka menu yang ingin dijalankan: '))
            print()
            if Input=='1':
                while True:
                    Input_Cari_ID=str(input('Masukan nomor ID yang ingin anda update (001-999): '))
                    print()
                    if Input_Cari_ID.isnumeric()==True and 0<int(Input_Cari_ID)<1000:
                        if ('ID'+Input_Cari_ID) not in Dictionary.keys():
                            print('================================================\n')
                            print('ID yang anda masukan tidak terdaftar\n')
                        else:
                            Fungsi_Print_Detail_Karyawan()
                            while True:
                                Fitur3_Update_Data=str(input('Update data? (Y/N) '))
                                print()
                                if Fitur3_Update_Data.upper()=='Y':
                                    while True:
                                        Key=str(input('Masukan data yang akan di update: '))
                                        print()
                                        if Key.upper()=='ID':
                                            print('================================================\n')
                                            print(f'"{Key.upper()}" tidak dapat diubah.\n')
                                            print('================================================\n')
                                        elif Key.title() in Dictionary['ID'+Input_Cari_ID].keys():
                                            Value=str(input('Masukan data baru: '))
                                            print()
                                            if Key.title()=='Nama':
                                                Confirm=input(f'Ubah {Key.title()} jadi "{Value.title()}" ? (Y/N) ')
                                                print()
                                                if Confirm.title()=='Y':
                                                    Dictionary['ID'+Input_Cari_ID][Key.title()]=Value.title()
                                                    Fungsi_Print_Data_Berhasil('update')
                                                    break
                                                elif Confirm.title()=='N':
                                                    break
                                            elif Key.title()=='Age':
                                                if Value.isnumeric()==True:
                                                    Confirm=input(f'Ubah {Key.title()} jadi "{Value.title()}" ? (Y/N) ')
                                                    print()
                                                    if Confirm.title()=='Y':
                                                        Dictionary['ID'+Input_Cari_ID][Key.title()]=Value.title()
                                                        Fungsi_Print_Data_Berhasil('update')
                                                        break
                                                    elif Confirm.title()=='N':
                                                        break
                                                else:
                                                    print('================================================\n')
                                                    print('Input Salah. Age hanya dapat berupa angka.\n')
                                                    print('================================================\n')
                                            elif Key.title()=='Sex':
                                                if Value.title()=='L' or Value.title()=='P':
                                                    Confirm=input(f'Ubah {Key.title()} jadi "{Value.title()}" ? (Y/N) ')
                                                    print()
                                                    if Confirm.title()=='Y':
                                                        Dictionary['ID'+Input_Cari_ID][Key.title()]=Value.title()
                                                        Fungsi_Print_Data_Berhasil('update')
                                                        break
                                                    elif Confirm.title()=='N':
                                                        break
                                                else:
                                                    print('================================================\n')
                                                    print('Input Salah. Sex hanya dapat diubah menjadi "L" atau "P".\n')
                                                    print('================================================\n')
                                            elif Key.title()=='Divisi':
                                                Confirm=input(f'Ubah {Key.title()} jadi "{Value.title()}" ? (Y/N) ')
                                                print()
                                                if Confirm.title()=='Y':
                                                    Dictionary['ID'+Input_Cari_ID][Key.title()]=Value.title()
                                                    Fungsi_Print_Data_Berhasil('update')
                                                    break
                                                elif Confirm.title()=='N':
                                                    break
                                        else:
                                            print('================================================\n')
                                            print(f'Tidak ada data "{Key}".\n')
                                            print('================================================\n')
                                    break
                                elif Fitur3_Update_Data.upper()=='N':
                                    break
                            Fungsi_Print_Menu_List_Karyawan()
                        break
                    else:
                        Fungsi_Print_Format_ID_Salah()
            elif Input=='2':
                break
            else:
                Fungsi_Print_Input_Salah()
    elif Input=='4':
        while True:
            Fungsi_Print_Sub_Menu_Other('delete')
            Input=str(input('Masukan angka menu yang ingin dijalankan: '))
            print()
            if Input=='1':
                while True:
                    Input_Cari_ID=str(input('Masukan nomor ID yang ingin anda delete (001-999): '))
                    print()
                    if Input_Cari_ID.isnumeric()==True and 0<int(Input_Cari_ID)<1000:
                        if ('ID'+Input_Cari_ID) not in Dictionary.keys():
                            print('================================================\n')
                            print('ID yang anda masukan tidak terdaftar\n')
                        else:
                            Fungsi_Print_Detail_Karyawan()
                            while True:
                                Fitur3_Hapus_Data=str(input('Hapus data? (Y/N) '))
                                print()
                                if Fitur3_Hapus_Data.upper()=='Y':
                                    Dictionary.pop('ID'+Input_Cari_ID)
                                    Fungsi_Print_Data_Berhasil('delete')
                                    break
                                elif Fitur3_Hapus_Data.upper()=='N':
                                    break
                            Fungsi_Print_Menu_List_Karyawan()
                        break
                    else:
                        Fungsi_Print_Format_ID_Salah()
            elif Input=='2':
                break
            else:
                Fungsi_Print_Input_Salah()
    elif Input=='5':
        print('Terima kasih.\n')
        break
    else:
        Fungsi_Print_Input_Salah()