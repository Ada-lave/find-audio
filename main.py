import moviepy.editor
path = input('Введите путь до файла (Не забудьте дописать в конце формат видео )\n')
finish = input('Введите куда файл распаковать (Не забудьте указать в какой аудио формат вы хотите переделать)\n')
video =moviepy.editor.VideoFileClip(path)
audio = video.audio
audio.write_audiofile(finish)