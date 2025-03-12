from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != 'POST':
        # 显示空表单
        form = UserCreationForm()
    else:
        # 处理填好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 登录用户
            login(request, new_user)
            return redirect('learning_logs:index')

    # 显示空表单或显示错误信息
    context = {'form': form}
    return render(request, 'registration/register.html', context)