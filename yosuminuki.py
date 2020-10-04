import PIL.Image
#import Image, ImageFilter, ImageDraw
#import PIL
import os
import glob
#from glob import glob
'''
print('test')
pp = os.getcwd()
print(pp,'getcwd')
os.chdir('Desktop')
pp = os.getcwd()
print(pp,'os.chdir')
'''
if os.path.exists('デスクトップ'):
    os.chdir('デスクトップ')
if os.path.exists('Desktop'):
    os.chdir('Desktop')
if os.path.exists('desktop'):
    os.chdir('desktop')
pp = os.getcwd()
pp = pp + '/四隅抜き'
#print(type(pp))
#print(pp)
for file in glob.glob(pp+'/画像置き場/'+'*.jpg'):
    #print('test1')
    im_rgb = PIL.Image.open(file)
    path = file.split('/')
    print(path[-1])
    im_rgba = im_rgb.copy()
    im_a = PIL.Image.open(pp+'/マスク画像置き場（変更ダメ）/'+'KOIRU.png').convert('L').resize(im_rgb.size)
    im_rgba.putalpha(im_a)
    savepath1 =  pp + '/白枠なし/'
    savepath2 =  pp + '/白枠あり/'
    aaa = path[-1].split('/')
    savepath1 = savepath1 + aaa[0] + '.png'
    savepath2 = savepath2 + aaa[0] + '.png'
    im_rgba.save(savepath1)
    #print('test2')
    
    ##### ここから
    
    im_b = PIL.Image.open(pp+'/マスク画像置き場（変更ダメ）/'+'KOIRU2.png')
    im_a = PIL.Image.open(pp+'/マスク画像置き場（変更ダメ）/'+'KOIRU5.png').convert('L').resize(im_b.size)
    im_d = PIL.Image.open(pp+'/マスク画像置き場（変更ダメ）/'+'KOIRU.png').resize(im_b.size)
    im_c = im_rgb.resize((int(im_b.size[0]*0.975),int(im_b.size[1]*0.98)))
    im_d.paste(im_c,(24,26))
    im_rgba = im_d
    im_rgba.putalpha(im_a)
    back_im = im_b.copy()
    im_rgba.save(savepath2)
    #print('test3')
    os.remove(file)

